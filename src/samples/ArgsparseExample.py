import argparse

###############################################################################
# How to process positional parameters
###############################################################################

# parser = argparse.ArgumentParser()
#
# parser.add_argument("mul_1",
# type=int,
# help="Enter first number")
#
# parser.add_argument("mul_2",
#                     type=int,
#                     help="Enter second number")
#
#
# args = parser.parse_args()
#
# print '-'*80
# print parser.print_help()
# print '-'*80
#
# print args.mul_1 * args.mul_2

###############################################################################
# How to process optional arguments
###############################################################################

# parser1 = argparse.ArgumentParser()
# parser1.add_argument('-v',
#                      "--verbose",
#                      help="setup verbosity"
#                      ,action="store_true") # when this value is specified, you do not need to provide value,
#                                           # You can use --verbose as flag
#
#
# args = parser1.parse_args()
#
# if args.verbose:
#     print "verbosity is on buddy: "

###############################################################################
# How to process positional and optional arguments
###############################################################################

# parser2 = argparse.ArgumentParser()
# parser2.add_argument("square"
#                      , type=int
#                      , help="Find square of the number")
#
# parser2.add_argument('-v'
#                      , '--verbose'
#                      , type=int
#                      , help="sho verbose output"
#                      , choices=[0, 1])
#
# args = parser2.parse_args()
#
# if args.verbose == 1:
#     print "Square of {} is {}".format(args.square, args.square ** 2)
# else:
#     print args.square ** 2

###############################################################################
# How to use default values for positional and optional arguments
###############################################################################

# parser3 = argparse.ArgumentParser()
#
# parser3.add_argument("number1", default=9, type=int, )
# parser3.add_argument('--number2', default=9, type=int)
#
# args = parser3.parse_args()`
# print args.number1 * args.number2

###############################################################################
# How to use default values for positional and optional arguments
###############################################################################

# parser4 = argparse.ArgumentParser()
# mutex_group_1=parser4.add_mutually_exclusive_group()
# mutex_group_1.add_argument ("-q",help="q it",action="store_true")
# mutex_group_1.add_argument ("-v",help="v it", action="store_true")
#
# mutex_group_2=parser4.add_mutually_exclusive_group()
# mutex_group_2.add_argument("--salsa",help="eat salsa", dest="salsa_type") # IMPO: ASSIGN TO ANOTHER VARIABLE
# mutex_group_2.add_argument("--milk",help="eat milk")
#
# ##### IMPO: THIS IS HOW YOU TEST WHAT VALUES WILL GO IN THE args
# print parser4.parse_args(['-q','--salsa','hot'])

###############################################################################
# More advanced use cases
###############################################################################

# Run the below module with command line args: -s SIMPLE -c -t -f -a rmwspc.py -a manveen -a avreen -A -B
# parser = argparse.ArgumentParser()
#
# parser.add_argument('-s', action='store', dest='simple_value',
#                     help='Store a simple value')
#
# parser.add_argument('-c', action='store_const', dest='constant_value',
#                     const='value-to-store',
#                     help='Store a constant value')
#
# parser.add_argument('-t', action='store_true', default=False,
#                     dest='boolean_switch',
#                     help='Set a switch to true')
#
# parser.add_argument('-f', action='store_false', default=False,
#                     dest='boolean_switch',
#                     help='Set a switch to false')
#
# parser.add_argument('-a', action='append', dest='collection',
#                     default=[],
#                     help='Add repeated values to a list',
#                     )
#
# parser.add_argument('-A', action='append_const', dest='const_collection',
#                     const='value-1-to-append',
#                     default=[],
#                     help='Add different values to list')
#
# parser.add_argument('-B', action='append_const', dest='const_collection',
#                     const='value-2-to-append',
#                     help='Add different values to list')
#
# parser.add_argument('--version', action='version', version='%(prog)s 1.0')
#
# results = parser.parse_args()
#
# print 'simple_value     =', results.simple_value
# print 'constant_value   =', results.constant_value
# print 'boolean_switch   =', results.boolean_switch
# print 'collection       =', results.collection
# print 'const_collection =', results.const_collection


###############################################################################
# Create groups that are NOT mutually exclusive, instead they are shown together
# in the help text
###############################################################################

# parser = argparse.ArgumentParser()
#
# group = parser.add_argument_group('authentication')
# group.add_argument('--user', action="store")
# group.add_argument('--password', action="store")
#
# group1 = parser.add_argument_group('hadoop')
# group1.add_argument("--fs")
# group1.add_argument("--namenode")

###############################################################################
# How to use nargs
###############################################################################

## Run with command line args: --three 1 2 3 --optional 1 --zero_or_more 0or1  --one_or_more 1 2 3 4 5
# parser5 = argparse.ArgumentParser()
# parser5.add_argument('--three', nargs=3)
# parser5.add_argument('--optional',nargs='?')
# parser5.add_argument('--zero_or_more',nargs='*')
# parser5.add_argument('--one_or_more',nargs='+')
# print parser5.parse_args()

###############################################################################
# Argument Type
###############################################################################

# parser6 = argparse.ArgumentParser()
#
# parser6.add_argument('-i', type=int)
# parser6.add_argument('-f', type=float)
# parser6.add_argument('--file', type=file)
#
# try:
#     print parser6.parse_args()
# except IOError, msg:
#     parser6.error(str(msg))

###############################################################################
# How to make an argument required
###############################################################################

parser.add_argument('--input-schema', dest='input_schema'
                        , help='Remove all spaces with no space',
                        action="store",
                        required = True)
parser.add_argument('--output-schema', dest='output_schema'
                        , help='Remove all spaces with no space',
                        action="store",
                        required = True)
