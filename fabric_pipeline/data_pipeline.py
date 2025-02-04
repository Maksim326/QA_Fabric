try:
    from QA_Venom.decorators import check_raw_table
except ImportError:
    def check_raw_table(func):
        return func

#Test decorator
@check_raw_table
def create_raw_rable():
    print("Creating raw table...")
    return True