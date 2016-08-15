#!/usr/bin/env python
# encoding: utf-8
"""
example.py

Created by Ben Birnbaum on 2012-12-02.
benjamin.birnbaum@gmail.com

Example use of outlierdetect.py module.
"""

from matplotlib import mlab
import outlierdetect
import pandas as pd


DATA_FILE = 'example_data.csv'

import operator

def print_scores(scores):
    for interviewer in scores.keys():
        print "%s" % interviewer
        sorted_scores = sorted(scores[interviewer].items(), key=operator.itemgetter(1), reverse=True)
        max_key = sorted_scores[0][0]

        print "\t Max suspicious column: %s" % max_key
        print "\t All interviewer scores for this column:"
        for interviewer2 in scores.keys():
            print "\t\t%s:\t%0.2f" % (interviewer2, scores[interviewer2][max_key])

        for score in sorted_scores[:5]:
            print "\t%s:\t%.2f" % score


if __name__ == '__main__':
    data = pd.read_csv(DATA_FILE)  # Uncomment to load as pandas.DataFrame.
    # data = mlab.csv2rec(DATA_FILE)  # Uncomment to load as numpy.recarray.

    # Compute SVA outlier scores.
    (sva_scores, agg_col_to_data) = outlierdetect.run_sva(data, 'interviewer_id', ['cough', 'fever'])
    print "SVA outlier scores"
    print_scores(sva_scores)

    # Compute MMA outlier scores.  Will work only if scipy is installed.
    (mma_scores, agg_col_to_data) = outlierdetect.run_mma(data, 'interviewer_id', ['cough', 'fever'])
    print "\nMMA outlier scores"
    print_scores(mma_scores)
