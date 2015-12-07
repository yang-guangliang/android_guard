##Introduction

This is a compact version of Androguard. More details about androguard are shown here:
	
 - https://code.google.com/p/androguard/w/list
 - https://github.com/androguard/androguard

## Updated at 10/12/2015:
 
 - Add a flag to control when to print instructions' detailed information
  - androguard.core.bytecodes.dvm: PRINT_INSTRUCTION_DETAILS_FLAG


## Updated at 10/09/2015:
 
 - Add three methods to DalvikVMFormat
  - get_all_methods_with_annotations()	: return a dictionary saving all methods that has annotations
  - parse_EncodedAnnotation()
  - parse_EncodedArray()
 - Add a new field to EncodedMethod
  - .annotation	: to save method's annotation in the future
