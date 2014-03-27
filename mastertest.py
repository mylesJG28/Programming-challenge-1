import multiples
import unitest

class TestSequanceFunctions(unitest.TestCase):

    def test1(self):
        multiples.mults(5,20)==[5,10,15] #test 1 fails
       
        if __name__ == '__main__':
    unittest.main()