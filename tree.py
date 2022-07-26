from re import sub

from packaging import version

class Node:
    def __init__(self, package, version, tags, parent, children, depth):
        self.package = package
        self.version = version[1:] # remove "v" from v1.2.3
        self.tags = tags
        self.parent = parent
        self.children = []
        self.depth = depth
        self.previous = None # TO BE ADDED

    def __str__(self, level = 0):
        str_rep = "\t" * level + f"{self.package} {self.version} {self.tags}" + "\n"
        for child in self.children:
            str_rep += child.__str__(level + 1)
        return str_rep

    def __repr__(self):
        return f"{self.package} {self.version} {self.tags}"



class Tree:
    def __init__(self, cargo_raw, project = None, root = None):
        self.project = project
        self.root = root
        self.size = 0
        self.build_from_cargo(cargo_raw)

    def bfs_hash_it(self, hmap):
        queue = [self.root]
        while queue:
            p = queue.pop(0)
            package_name = p.package
            p_version = p.version
            depth = p.depth

            if package_name not in hmap and depth != 0:
                hmap[package_name] = p_version

            if package_name in hmap:
                h_version = hmap[package_name] #tie breaker is highest package
                if version.parse(p_version) > version.parse(h_version):
                    hmap[package_name]=p_version
            children = p.children 
            if children:
                for child in children:
                    queue.append(child)


    def bfs_update(self, hmap, newhmap):
        queue = [self.root]
        while queue:
            p = queue.pop(0)
            package_name = p.package
            current_version = p.version
            if package_name in hmap:
                anchor_version = hmap[package_name]
                if version.parse(anchor_version) > version.parse(current_version):
                    p.version= anchor_version
                    p.previous = current_version
                    if package_name not in newhmap:
                        newhmap[package_name] =anchor_version

            children = p.children 
            if children:
                for child in children:
                    queue.append(child)
 
 

    @classmethod
    def get_depth(cls, str):
        return  len(str.rstrip()) - len(str.lstrip())

    def build_from_cargo(self, cargo_raw):
        stripped_cargo_raw = sub("[^\w\s\.\(\)\*\-]+", "", cargo_raw) 
        stripped_cargo_raw = stripped_cargo_raw.strip() 
        tree_body = stripped_cargo_raw.split("\n") 
        ptr = None
        kinds = []
        for line in tree_body:
            line = line.rstrip()
            dep = line.lstrip().split(" ")        
            depth = Tree.get_depth(line)

            if len(dep) == 1:
                kinds.append((depth, dep[0]))
            else:
                package_name, version, *tags = dep
                node = Node(package_name, version, tags, "", [], depth)                
                if not self.root:
                    self.project = package_name
                    self.root = node
                    ptr = self.root
                else:
                    if depth > ptr.depth:
                        node.parent = ptr
                        ptr.children.append(node)
                        ptr = node
                    elif depth == ptr.depth:
                        node.parent = ptr.parent
                        ptr.parent.children.append(node)
                        ptr = node
                    else:
                        while ptr.depth > depth:
                            ptr = ptr.parent
                        node.parent = ptr.parent
                        ptr.parent.children.append(node)
                        ptr = node
                if kinds:
                    curr_kind = kinds[-1]
                    if node.depth > curr_kind[0]:
                        node.tags.append(curr_kind[1])
                    else:
                        kinds.pop(-1)
                    

    def __str__(self):
        return str(self.root)
    
    @classmethod
    def to_ascii(cls, node, curr_id, prefix = ""):
        def format_tree(node, curr_id, prefix = "", ls = []):
            connector = "└── " 
            if node.depth != 0:
                if node != node.parent.children[-1]:
                    connector = "├── "
            st = f"{prefix}{connector}"
            st += repr(node)
            ls.append(st + "\n")
            children = node.children
            for child in children:
                new_prefix = prefix
                if node.depth != 0:
                    if node == node.parent.children[-1]:
                        new_prefix += "    "
                    else:
                        new_prefix += "│   "
                format_tree(child, curr_id, new_prefix, ls)
            return ls
        tree = format_tree(node, curr_id, "", [])
        return tree
    
