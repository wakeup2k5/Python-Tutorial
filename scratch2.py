def main(): 

    dictionary={"a": "apple", "b":"banana"} 

    key="b" 

    value_extracted_successfully = False

    try:
        value_to_print = dictionary[key]
        value_extracted_successfully = True
    except (KeyError):
        value_extracted_successfully = False
    finally:
        print('Outcome: ' + str(value_extracted_successfully))
    
    
    return value_extracted_successfully
  

main() 