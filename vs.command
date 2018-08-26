#! /bin/bash
apppath=`greadlink -f $0`
python `dirname $apppath`/run_search.py