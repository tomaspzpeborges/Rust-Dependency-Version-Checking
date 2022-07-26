import subprocess, os, sys, argparse, pathlib, glob


base_path = pathlib.Path(__file__).parent.resolve()


def run_cargo_tree(project):

    os.chdir(project)
    is_rust = False
    print("looking in: "+project)

    #for file in os.listdir(project):
    if glob.glob('Cargo.toml'):
        is_rust = True
    print("is rust? "+str(is_rust))
    
    if is_rust:
        tree = subprocess.run(["cargo tree"],shell=True)
        os.chdir(base_path.parent)
        return tree
    else:
        print("project {} is not written in rust".format(project))
        os.chdir(base_path.parent)
        return None



def main():

    print(base_path.parent)

    os.chdir(base_path.parent)

    parser = argparse.ArgumentParser()
    parser.add_argument('anchor_project_path', help = "the anchor project; will not be updated")
    parser.add_argument('comparable_project_path', help = "the project to be compared; will be updated according to the dependencies of the anchor project")

    args = parser.parse_args()

    A_tree = run_cargo_tree(args.anchor_project_path)
    B_tree = run_cargo_tree(args.comparable_project_path)

    #print("first tree: "+A_tree)
    #print("second tree: "+B_tree)

if __name__ == "__main__":
    main()

