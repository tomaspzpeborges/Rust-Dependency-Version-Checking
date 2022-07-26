import subprocess, os, sys, argparse, pathlib, glob
from tree import Tree


base_path = pathlib.Path(__file__).parent.resolve()


def run_cargo_tree(project):

    os.chdir(project)
    is_rust = False
    print("looking in: "+project)

    #for file in os.listdir(project):
    if glob.glob('Cargo.toml'):
        is_rust = True
    #print("is rust? "+str(is_rust))
    
    if is_rust:
        tree = subprocess.run(["cargo tree -q"],shell=True)
        os.chdir(base_path.parent)
        return tree
    else:
        print("project {} is not written in rust".format(project))
        os.chdir(base_path.parent)
        return None


def run_cargo_build(project):

    os.chdir(project)
    is_rust = False

    if glob.glob('Cargo.toml'):
        is_rust = True

    if is_rust:
        build = subprocess.run(["cargo build"],shell=True)
        os.chdir(base_path.parent)
        return build
    else:
        print("project {} is not written in rust".format(project))
        os.chdir(base_path.parent)
        return None

def run_cargo_update(dep_dict, project):

    os.chdir(project)

    for item in dep_dict:
        print(item)
        subprocess.run(["cargo update -p "+item+" --precise "+dep_dict[item]], shell=True)
    
    os.chdir(base_path.parent)
    return None

def main():

    print(base_path.parent)

    os.chdir(base_path.parent)

    parser = argparse.ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument('-a', help = "the anchor project; will not be updated")
    parser.add_argument('-c', help = "the project to be compared; will be updated according to the dependencies of the anchor project")
    parser.add_argument('-b', '--build', help = "runs cargo build on the updated project", required = False)

    args = parser.parse_args()

    A_tree = run_cargo_tree(args.a)
    B_tree = run_cargo_tree(args.c)

    a_tree = Tree(str(A_tree))
    b_tree = Tree(str(B_tree))
    hmap = {}
    a_tree.bfs_hash_it(hmap)
    #print(hmap)
    #print()
    newhmap = {}
    b_tree.bfs_update(hmap, newhmap)
    #print(str(tree2))
    
    print(newhmap)
    #print(*tree.to_ascii(tree.root, -1))


    if args.build:
        run_cargo_build(args.c)

    #dictionary = {"ahash": "0.7.5" , "aho-corasick" : "0.7.17" , "anyhow" : "1.0.57"}
    run_cargo_update(newhmap, args.c)

    print("new tree: ")

    new_tree = run_cargo_tree(args.c)


if __name__ == "__main__":
    main()

