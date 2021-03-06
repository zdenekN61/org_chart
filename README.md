# Org chart

## Development environment
- Windows 10 Home
- Vim 7.4
- Python 3.5.3

## Description
Test HW for an interview.

## How to use
python org_chart.py orgchart.csv employees.csv

## Params
	-- orgchart.csv - file contains company orgchart data(see test_data directory)  
	-- employees.csv - file contains employees data(test_data directory)  

## Strusture of files(params)
##**orgchart(collums):**
	
**_ID_** - ID of department(mandatory).  
**_Parent-ID_** - ID of its parent department -> superior department. If ID does not exist -> department on top level(NOT-mandatory).  
**_Deparment Name_** - Name of department(mandatory).  
**_Deparment City_** - City of residency(mandatory).  


##**employees(collums):**

**_ID_** - ID of employee(mandatory).  
**_Firstname_** - :)(mandatory).  
**_Surname_** - :)(mandatory).  
**_Department-ID_** - ID of department where employee belong(mandatory).  
**_Birth date_** - :)(mandatory).  
	
For closer look(to make a picture) see test_data directory.  

## Supported user commands  
**Department 5** -> name of department for given departmentīs ID.  
**Count 1** -> number of employees(+sub-departs) for given departmentīs ID.  
**People 1** -> names of employees(+sub-departs) for given departmentīs ID.  
**Avgage 1** -> average age of employees(+sub-departs) for given departmentīs ID.  
**Help** -> show help(supported command).  
**Exit** -> Exit.  

## Example - result for command over test data from 'test_data' directory  
Department 1  
*output:* Delivery, Brno  
Department 10  
*output:* Testing, Moskva  

Count 1  
*output:* 6  
Count 10  
*output:* 1  

People 1  
*output:* Jodie Foster, Petr Pavel, John Wayne, Jana Hvezdova, Petr Kral, Adina Mandlova,  
People 5  
*output:* Jodie Foster, Petr Pavel,  

Avgage 1  
*output:* 63.78 years  
Avgage 5  
*output:* 43.14 years
