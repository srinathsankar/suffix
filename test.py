import suffix_tree as st
import regex as re
import random
import string
import collections
def create_suffix_tree(text):
    #Create a suffix tree
    sTree = st.Tree({"inputText":text}, builder=st.ukkonen.Builder)
    return sTree
def traverse_tree(root,text,sTree):
    repeating_substrings = {}
    def node_traversal(node,sTree):
        #print("\n")
        #if not node: return i
        if hasattr(node,'children'):
            print("\nNode label: " + text[node.start:node.end], end = "\t")
            #check if it has any leaf children
            if any(not hasattr(child,'children') for child_label,child in node.children.items()):
                indices_list = [i[1].start for i in sTree.find_all(text[node.start:node.end])]
                print(indices_list)
                repeating_substrings[text[node.start:node.end]] = (indices_list,text[node.start:node.end],node)
                print("Repeating substring")
                #check if it has a suffix link upon construction
                #if node.suffix_link: print("Node has suffix link: ",node.suffix_link, end = "\t")
            for child_label, child in node.children.items():
                #iterate through its children

                node_traversal(child,sTree)
        else: 
            #is leaf node
            #print("Node label: " + text[node.start:node.end] + "$") #add dollar for termination symbol
            
            #print("no child")
            return
        #return repeating_substrings

    node_traversal(root,sTree)
    return repeating_substrings
def find_all_occurences(tree,subtext):

    tree.find(subtext)
    tree.find_all(subtext)
def generate_random_strings(min_length, max_length):
    length = random.randint(min_length,max_length)
    randomString = ''.join(random.choice(['a','b','c','d','e']) for _ in range(length))
    return randomString
def generate_overlapping_strings():
    overlap = generate_random_strings(1,3)
    non_overlap = generate_random_strings(0,2)
    repeat = random.randint(1,5)
    overlapping_repeating_string = overlap + (non_overlap + overlap + non_overlap)*repeat + overlap
    return (overlapping_repeating_string,overlap,non_overlap,repeat)
def contains_only_repetitions(string, substring):
    pattern = f"^(?:{substring})+$"
    return re.fullmatch(pattern, string) is not None
def suffix_link_tester():
    l = 10000
    hit = 0
    miss = 0
    for i in range(10000):
        s,o,n,r = generate_overlapping_strings()
        print("BEING PROCESSED: ", s)
        sTree = create_suffix_tree(s)
        d = traverse_tree(sTree.root,s,sTree)
        #print(d)
        #if contains_only_repetitions(s, o + n):
        #    print("SPECIAL CASE: ", s)
        #    continue
        
        try:
            print("> Overlapping subtring " + o + (n + o)*(r) + " has suffix link?: ", d[o + (n + o)*(r)][2].suffix_link, (o,n,s,r))
            hit += 1
            #print("> Occurences of d[o+n+o]: ",len([i.start for i[1] in sTree.findall(o + n + o)]))
        except KeyError:
            print("> Failed! no suffix link for ", (o,n,s,r), ". That is, no ", o + (n + o)*(r), " in ", s, " ", d.keys())
        except Exception as e:
            print(e)
    print("Processed no of strings for suffix links: ", l)
    print(hit)
    print("> suffix link Success rate is: ", 100*(hit)/l)
def concept_tester():
    text = input("Enter text: ")
    sTree = create_suffix_tree(text)
    print(sTree)
    d = traverse_tree(sTree.root,text,sTree)
    print(d.items())
    '''
    for key, value in d.items():
        print(key)
        print(sTree.find_all(value[1]))
    '''
def check_if_overlap():
    input_string = input("Enter String:")
    substring = input("Enter Substring:")
    sTree = create_suffix_tree(input_string)
    indices_list = sTree.find_all(substring)
    print(indices_list)
    for i in range(len(indices_list)-1):
        first_start = indices_list[i][1].start
        second_substring_start = indices_list[i + 1][1].start
        print(f"First start: {first_start}, second substring start: {second_substring_start}")
        print(indices_list[i][1].start,indices_list[i + 1][1].start)
        if first_start + len(substring) - 1 >= second_substring_start:
            return True
    return False

def overlap_remove(s):
    raise NotImplementedError



suffix_link_tester()
#concept_tester()
#print(check_if_overlap())
