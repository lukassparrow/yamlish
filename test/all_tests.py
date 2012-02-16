import unittest
import test_load
import test_input
#import test_reader
import test_output
#import test_writer

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_load)
    suite.addTests(loader.loadTestsFromModule(test_input))
    #suite.addTests(loader.loadTestsFromModule(test_reader))
    suite.addTests(loader.loadTestsFromModule(test_output))
    #suite.addTests(loader.loadTestsFromModule(test_writer))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
