# aws-healthomics-stepfunctions

Reqs:
Trigger a set of parallel running “primary processing” workflows for each
sample in a flowcell.
 Once all primary processing workflows are complete, trigger a “QC”
workflow for the flowcell.
 Primary processing workflow can fail independently and should not affect
the processing of other workflows (including QC).
 Primary processing workflows may have varying completion times.
 Provide the ability to monitor the status of processing of the entire flowcell
(start to finish of QC) as well as status of individual sample primary
processing.

