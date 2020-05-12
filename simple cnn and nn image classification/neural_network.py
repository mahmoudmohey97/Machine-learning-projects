from keras.models import Sequential
from keras.layers import Dense, Flatten


class NeuralNetworkArchitectures:
    def __init__(self, shape):
        self.shape = shape

    def createModelNN4(self):
        model = Sequential()
        model.add(Flatten(input_shape=self.shape))
        model.add(Dense(200, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def createModelNN3(self):
        model = Sequential()
        model.add(Flatten(input_shape=self.shape))
        model.add(Dense(256, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def createModelNN2(self):
        model = Sequential()
        model.add(Flatten(input_shape=self.shape))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model


    def createModelNN1(self):
        model = Sequential()
        model.add(Flatten(input_shape=self.shape))
        # model.add(Dense(128, activation='relu'))
        # model.add(Dense(64, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model


    def choose(self, i):
        if i == 1:
            return self.createModelNN1()
        if i == 2:
            return self.createModelNN2()
        if i == 3:
            return self.createModelNN3()
        if i == 4:
            return self.createModelNN4()
        else:
            return 0
