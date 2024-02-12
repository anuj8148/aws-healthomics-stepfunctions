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

![CarisPoC-Page-2 drawio](https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/bd7b77cb-5489-4c89-9909-74d22d5bc1c1)
<img width="730" alt="carispocmetadatainput" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/626def2e-3fc7-442c-b67b-19bcb3156b24">

<img width="714" alt="carispocsampleworkflowinput" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/a0f6f621-587e-4848-b7b4-52ebf9fd700d">

<img width="141" alt="CarisPoCStepFunctions" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/331a2e7a-1232-43ed-9c99-57d2ed779d85">
<img width="403" alt="stepfunctionsexecution" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/f5500ebc-8433-4e62-ae8c-0ebe919f9a40">

<img width="899" alt="healthomicsruns" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/13bd64a9-a013-476d-afa2-e02518990fe4">

<img width="718" alt="carispocsampleworkflowoutput" src="https://github.com/anuj8148/aws-healthomics-stepfunctions/assets/159836702/a64a8d1e-da23-4ab6-a138-921f60d615f2">
