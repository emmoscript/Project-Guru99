## QA Testing Project 1
### Guru99 - Demo Banking Site Automation Testing
This Guru99 project is to ensure that all the features and functionalities of demo banking software run smoothly providing a good banking experience to end users. Banking software performs various functions like transferring and depositing funds, balance inquiry, transaction history, withdrawal and so on.

#### Test Cases
1. Test Cases deal with Login Page Feature
2. Test Cases deal with Home Page Feature
3. Test Cases deal with Balance Enquiry

#### POM Pattern
1. Test Codes stores Test Files (i.e. test_login, test_pim, etc.,)
2. Test Data stores Test Data (i.e. username, password, XPATH, ID, etc.,)
3. Configuration Files
4. Test Reports
5. Excel Files

#### Execution Command
```
pytest -v -s --capture=sys --html=test_results/report.html (Path to save HTML reports)
```

