

def convert_to_str(input_seq, separator):
    try:
        final_str = separator.join(input_seq)
        return final_str
    except Exception as e:
        print(f'convert_to_str - {e}')
        exit()
