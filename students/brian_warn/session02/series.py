#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# series.py

def main():
    def fibonacci(n):
        ''' Compute fibonacci series for a given input number
        :arg input integer
        :return: nth value in the fibonacci series
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    def lucas(n):
        ''' Compute Lucas Numbers series for a given input number
        :arg input integer
        :return: nth value in the Lucas Numbers series
        '''
        if n == 0:
            return 2
        if n == 1:
            return 1
        return luc(n - 1) + luc(n - 2)

    def sum_series(n, a = 0, b = 1):
        ''' Compute Lucas Numbers series or Fibonacci series based upon optional parameter values
        :arg 
            n = input integer
            a = first optional argument
            b = second optional argument
        :return: nth value in either the Lucas Numbers series or Fibonacci series
        '''
        if a == 0 and b == 1:
            result = 'Fibonacci Sequence Result for ' + str(n) + ' is :' + fibonacci(n)
            return result

    def run_program():

        n_value = int(input("Input nth value to be computed: "))
        first_number = str(input("Provide the first number of the series: "))
        second_number = str(input("Provide the second number of the series: "))
        if first_number == '':
            first_number = int(0)
        if second_number == '':
            second_number = int(1)
        output = sum_series(n_value, first_number, second_number)
        print(output)

    run_program()

if __name__ == "__main__":
    main()
