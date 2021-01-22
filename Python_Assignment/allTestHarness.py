import graphMenuTestHarness
import fileIOTestHarness
import assetAndTradeTestHarness
import linkedListTestHarness
import bstTestHarness
import DSAStackTestHarness
import sys
import timeit
import psutil
import os

start = timeit.default_timer()

#graphMenuTestHarness.main()
#fileIOTestHarness.main()
#assetAndTradeTestHarness.main()
linkedListTestHarness.main()
bstTestHarness.main()
DSAStackTestHarness.main()


stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)

sys.stdout.write("Total running time: %d:%d (minutes:seconds)\n" % (mins, secs))