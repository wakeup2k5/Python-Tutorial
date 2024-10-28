
def main(): 

    ls=[16,9,8] 

    idx=2
    
    value_extracted_successfully = False

    try:
        value_to_print = ls[idx]
        value_extracted_successfully = True
    except:
        value_extracted_successfully = False
    finally:
        print('Outcome: ' + str(value_extracted_successfully))
    
    
    return value_extracted_successfully

  

main() 