import numpy as np
from operator import itemgetter
import csv, os

class KNNClassifier:
    def __init__(self):
        self.training_features = None  #movie kicks, kisses [[3,104], [], [], [], [], [] ]
        self.training_labels = None  # movie type ['Romance' , 'Romance', , , , ]

        self.test_features = None   #kicks=18 , kisses=90  [18,90]

        #Build meaningful result
        self.elegantResult = "Most likely, movie '{0}' is of type of '{1}'."

    def loadTrainingDataFromFile(self, file_path):
        if file_path is not None and os.path.exists(file_path):
            tr_features = []
            self.training_labels = []
            with open(file_path,'r') as training_data_file:
                reader = csv.DictReader(training_data_file)
                for row in reader:
                    if row['moviename'] == '?':
                        self.test_features=np.array(      [   float(row['kicks']),   float(row['kisses'])  ]      )
                    else:
                        tr_features.append( [ float(row['kicks']), float(row['kisses']) ]  )
                        self.training_labels.append( row['movietype'] )

            if len(tr_features) >0 :
                self.training_features = np.array(tr_features)

            print( "self.training_features : \n", self.training_features )
            print( "self.training_labels   : ",   self.training_labels )
            print( "self.test_features     : " ,  self.test_features )  #Question Data


                              #[1.1,1]
                              #[18, 90]          k=5

    def classifyTestData(self, test_data = None, k=0):
        print( "classifyTestData:  test_data : ", test_data )   #None
        if test_data is not None:
            self.test_features = np.array(test_data, dtype=float)
        print( "classifyTestData:  self.test_features : ", self.test_features )

        #ensure we have training data, trainig labels, test data and number of 'k'
        if self.test_features is not None and \
                        self.training_features is not None and \
                        self.training_labels is not None and k >0:

            print( "classifyTestData says self.test_features : ",self.test_features  )  #[ 18, 90 ]
            print( "self.training_features : \n", self.training_features )   #[ [3,104], [2,100], [1,81], [101,10], [99,5], [98,2] ]
            print( "self.training_labels : ", self.training_labels )         #['Romance',  'Romance'             ]
            featureVectorSize = self.training_features.shape[0]    #Answwer will be 6
            print( "featureVectorSize : ", featureVectorSize)     #featureVectorSize 6
            tileOfTestData = np.tile(self.test_features, (featureVectorSize,1) ) #[ [18,90],[18,90],[18,90],[18,90],[18,90],[18,90]]
            print( "after tileOfTestData : \n" , tileOfTestData )
            diffMat =  self.training_features - tileOfTestData
            print( "diffMat : \n", diffMat )
            sqDiffMat = diffMat ** 2
            print( "sqDiffMat : \n" , sqDiffMat  )   # 6 x 2
            sqDistances = sqDiffMat.sum(axis=1)  # 6 x 1 pruduce the row wise result of sum()
            print(  "(Row wise sum )sqDistances : " , sqDistances )
            distances = sqDistances ** 0.5
            print( "distances (square root of sqDistances): ", distances )
            sortedDistanceIndices = distances.argsort()          #sortedDistanceIndices = [ 1, 2, 0, 3, 4, 5 ]
            print( "sortedDistanceIndices : " , sortedDistanceIndices )
            print( "self.training_labels : ", self.training_labels )

            classCount = { }
            #sortedDistanceIndices = [ 1, 2, 0, 3, 4, 5 ]
            #                       i= 0  1  2  3  4

            for i in range(k):   # k = 5 == [0, 1, 2, 3, 4]
                print( "sortedDistanceIndices[",i,"] : ", sortedDistanceIndices[i] )
                voteILabel  = self.training_labels[sortedDistanceIndices[i]]
                print( "voteILabel  : ", voteILabel )  #voteILabel = "Action"
                classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

            #classCount = {"Action" :2 ,
            #              "Romance":3  }
            #                 0      1

            print( "classCount = ",classCount )
            sortedClassCount = sorted(classCount.items(), key=itemgetter(1), reverse=True )
            # sortedClassCount = [ ("Romance",3) , ("Action",2)  ]
            #                          0      1       0,     1
            #                            0             1
            print( "sortedClassCount = ", sortedClassCount )           #[ ("Romance",3) , ("Action",2)  ]
            print( "sortedClassCount[0] : ", sortedClassCount[0] )      #("Romance",3)
            print( "sortedClassCount[0][0] : ", sortedClassCount[0][0] ) #"Romance"
            return sortedClassCount[0][0]
        else:
            return "Due to incomplete data, Can't determine result."

def predictMovieType():
    instance =  KNNClassifier()
    instance.loadTrainingDataFromFile('LgR_Movies_kNN_classifier.csv')
    print( "****************************************" )

    #Example-01
    #Generate the output of question data provided in the data file
    # classOfTestData = instance.classifyTestData(test_data=None, k=5)

    #Example-02 (For Example-2, comment the previous line of code and uncomment following two lines of code)
    #Generate the output of custom question data provided within the code file
    #-----------------------------------------------------------
    my_test_data = [50, 50]  # can be supplied to instance.classifyTestData()




    classOfTestData = instance.classifyTestData(test_data=my_test_data , k=5)
    #-----------------------------------------------------------
    print( "predictMovieType### classOfTestData=", classOfTestData )
    return instance.elegantResult.format( str(instance.test_features),  classOfTestData)

if __name__ == '__main__':
    answer =  predictMovieType()
    print(answer)
