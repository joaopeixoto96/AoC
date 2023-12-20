import os
from icecream import ic
import re
from time import perf_counter
from typing import Set,Optional,List,Tuple

file_path = os.path.join('AoC_2023','day5.txt')
def clean_line(line: str) -> Tuple[int,int,int]:
    res = (int(x) for x in line.split())
    return res

'''Part 1'''


# seeds = ()
# locations = []

# try:
#     with open(file_path,'r') as file:
#         for line in file:
#             line = line.strip().split(':')[1]
#             seeds = (int(x) for x in line.split())
#             break

#         #now we have all the seeds, so lets go through the seeds
#         for seed_num in seeds:
#             node_num = seed_num
#             #so the node we start as is seed num, now we traverse everything else like a graph
#             des_found = False #this flag checks whether the destination has been found in the current mapping
#             for line in file:
#                 line = line.strip()
#                 if line == '' or "map" in line or "seeds" in line:
#                     des_found = False
#                     continue
#                 if des_found:
#                     continue
#                 des_ran_str,src_ran_str,ran_len = clean_line(line)
#                 interval = (src_ran_str,src_ran_str + ran_len - 1)
#                 if node_num >= interval[0] and node_num <= interval[1]:
#                     diff = src_ran_str-des_ran_str
#                     ic(node_num)
#                     node_num = node_num - diff
#                     ic(diff)
#                     ic(interval)
#                     ic(node_num)
#                     ic(des_ran_str)
#                     ic(src_ran_str)
#                     ic(ran_len)
#                     des_found = True
#             locations.append(node_num)
#             file.seek(0)
#         print(locations)
#         ic(min(locations))
# except FileNotFoundError:
#     print(f"file not found")


'''Part 2'''


def merge_intervals_special(intervalsA: List[Tuple[int, int, int]], intervalsB: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Merge two lists of intervals. Only overlapping intervals are considered.
    If an interval in intervalsB overlaps with intervalsA, it takes priority.
    Parts of intervalsB that do not overlap with any interval in intervalsA are dropped.
    """
    result = []

    for a_start, a_end, a_diff in intervalsA:
        a_index = a_start
        while a_index <= a_end:
            overlap_found = False
            for b_start, b_end, b_diff in intervalsB:
                if b_start <= a_index <= b_end:
                    # Overlap found, use intervalsB's diff
                    overlap_end = min(b_end, a_end)
                    result.append((a_index, overlap_end, b_diff))
                    a_index = overlap_end + 1
                    overlap_found = True
                    break
            
            if not overlap_found:
                # No overlap, use intervalsA's diff
                next_b_start = min([b_start for b_start, _, _ in intervalsB if b_start > a_index], default=a_end + 1)
                result.append((a_index, min(a_end, next_b_start - 1), a_diff))
                a_index = next_b_start

    return sorted(result, key=lambda x: x[0])

def merge_intervals(intervals: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Merge overlapping intervals based on their start and end values, 
    while preserving the identifier of the first interval in each merged pair.

    Args:
    intervals (List[Tuple[int, int, int]]): A list of intervals sorted by start value, 
                                            each with an identifier.

    Returns:
    List[Tuple[int, int, int]]: A list of merged intervals with their original identifiers.
    """
    if not intervals:
        return []

    # Initialize the merged intervals list with the first interval
    merged = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]

        # Check if the current interval overlaps with the previous interval (considering only the start and end)
        if current[0] <= previous[1]:
            # Merge the current interval with the previous one and keep the identifier of the first interval
            merged[-1] = (previous[0], max(previous[1], current[1]), previous[2])
        else:
            # No overlap, so add the current interval to the merged list
            merged.append(current)

    return merged

def get_seed_intervals(intervals: List[int]) -> List[Tuple[int,int]]:
    res = []
    for i in range(0,len(intervals),2):
        start = intervals[i]
        end = intervals[i] + intervals[i+1] - 1
        res.append((start,end))
    res.sort(key=lambda I: I[0]) #sort intervals by start, so we can merge them later
    res = merge_intervals(res)
    return res

def generate_srcintervals_withdiff(line: List[int]) -> List[Tuple[int,int,int]]:
    start = line[1]
    end = line[1] + line[2]-1
    diff = line[0] - line[1]
    return (start,end,diff)

def convert_src_to_dest(intervals: List[Tuple[int,int,int]]) -> List[Tuple[int,int,int]]:
    res = []
    for start_src,end_src,diff in intervals:
        res.append((start_src + diff, end_src + diff, 0))
    return res

def standardize_intervals(intervals: List[Tuple[int,int]],default_identifier = 0) -> List[Tuple[int,int,int]]:
    return [(start, end, default_identifier) for start,end in intervals]

def find_res_min(res: Tuple[int,int]) -> int:
    sol = float('inf')
    for a,b in res:
        if a < sol:
            sol = a
        if b < sol:
            sol = b
    return sol


if __name__ == '__main__':
    start_time = perf_counter()
    node_intervals = []
    locations = []
    current_intervals_source_and_diff : List[Tuple[int,int,int]] = [] #will be like so -> [(startsource,endsource,difference)] difference = destination-source


    try:
        with open(file_path,'r') as file:
            for line in file:
                line = line.strip().split(':')[1]
                node_intervals = [int(x) for x in line.split()]
                node_intervals = get_seed_intervals(node_intervals)
                node_intervals = standardize_intervals(node_intervals)
                # ic(node_intervals)
                break

            for line in file:
                line = line.strip()
                if line == '':
                    continue
                if "map" in line: #then process all lines in current map
                    for line in file:
                        line = line.strip()
                        if line == '' or "end" in line:
                            current_intervals_source_and_diff.sort(key=lambda V: V[0])
                            current_intervals_source_and_diff = merge_intervals(current_intervals_source_and_diff)
                            # ic(current_intervals_source_and_diff)
                            node_intervals = merge_intervals_special(node_intervals,current_intervals_source_and_diff)
                            # ic(node_intervals)
                            node_intervals = convert_src_to_dest(node_intervals)
                            # ic(node_intervals)
                            current_intervals_source_and_diff.clear()
                            break
                        this_interval = [int(x) for x in line.split()]
                        this_interval = generate_srcintervals_withdiff(this_interval)
                        current_intervals_source_and_diff.append(this_interval)
            locations.append(node_intervals)
            file.seek(0)
        res = []
        for node_str,node_end,diff in node_intervals:
            res.append((node_str + diff,node_end + diff))
        # ic(res)
        sol = find_res_min(res)
        print(f"closest location = {sol}")
                    
    except FileNotFoundError:
        print(f"file not found")

    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time} seconds")
