# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

CHUNK_SIZE = 5


def kthByExtreme(unsortedList, k):
    for ith in xrange(k):
        kth, unsortedList = removeSmallest(unsortedList)
    return kth


def kthBySorting(unsortedList, k):
    sorted_list = mergesort(unsortedList)
    kth = sorted_list[k - 1]
    return kth


def kthByMedianOfMedian(unsortedList, k):
    if len(unsortedList) <= CHUNK_SIZE:
        return get_kth(unsortedList, k)

    chunks = splitIntoChunks(unsortedList, CHUNK_SIZE)

    medians_list = []

    for chunk in chunks:
        median_chunk = get_median(chunk)
        medians_list.append(median_chunk)

    size = len(medians_list)
    mom = kthByMedianOfMedian(medians_list, size / 2 + (size % 2))
    smaller, larger = splitListByPivot(unsortedList, mom)
    valuesBeforeMom = len(smaller)

    if valuesBeforeMom == (k - 1):
        return mom
    elif valuesBeforeMom > (k - 1):
        return kthByMedianOfMedian(smaller, k)
    else:
        return kthByMedianOfMedian(larger, k - valuesBeforeMom - 1)


def kthByQuickSelect(unsortedList, k):
    pivot = random.choice(unsortedList)
    smaller, larger = splitListByPivot(unsortedList, pivot)
    valuesBeforePivot = len(smaller)
    if valuesBeforePivot == k - 1:
        return pivot
    elif valuesBeforePivot > k - 1:
        return kthByQuickSelect(smaller, k)
    else:
        return kthByQuickSelect(larger, k - valuesBeforePivot - 1)
