import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Global parameters
FILE_NAME = "C:/Users/zain ul hassan/PycharmProjects/DjangoProject/TeacherSelection/static/csv/data.csv"
CLASS_COL = 22
TEST_SIZE = 0.2
NUM_INPUTS = 22
ACT_HIDDEN = "sigmoid"
ACT_OUT = "softmax"
ERR_FUNC = "sparse_categorical_crossentropy"
NUM_EPOCHS = 500
BATCH_SIZE = 10

# Step#1
print("Step#1: Acquiring data")
df = pd.read_csv(FILE_NAME, header=0, usecols=[x for x in range(23)])
print("> Data acqruired. data.describe()")
print(df.describe(), end='\n\n')

# Step#2
print("Step#2: Encoding columns")
df = df.apply(preprocessing.LabelEncoder().fit_transform)
print("> Columns encoded to integer values. data.describe()")
print(df.describe(), end='\n\n')

# Step#3
print("Step#3: Splitting data")
x, y = df.iloc[:, :CLASS_COL], df.iloc[:, CLASS_COL]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE)
print("> Data splitted. x_train=" + str(x_train.shape) + ", x_test=" + str(x_test.shape) + ", y_train=" + str(
    y_train.shape) + ", y_test=" + str(y_test.shape), end='\n\n')

# Step#4
print("Step#4: Generating a shallow neural network")
model = Sequential()
model.add(Dense(22, input_shape=(NUM_INPUTS,), activation=ACT_HIDDEN))
model.add(Dense(20, activation=ACT_HIDDEN))
model.add(Dense(15, activation=ACT_HIDDEN))
model.add(Dense(13, activation=ACT_HIDDEN))
model.add(Dense(12, activation=ACT_OUT))
model.compile(loss=ERR_FUNC, optimizer='adam', metrics=['accuracy'])
print("> Network generated. model.summary()")
print(model.summary(), end='\n\n')

# Step#5
print("Step#5: Training the network with " + str(NUM_EPOCHS) + " epochs and " + str(BATCH_SIZE) + " batch size")
model.fit(x_train, y_train, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)
_, accuracy = model.evaluate(x_test, y_test)
print("> Training finished.")
print('> Final accuracy: %.2f' % (accuracy * 100))
