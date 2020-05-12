from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten,MaxPooling2D


class CNN:
    def __init__(self, shape):
        self.shape = shape

    def createModelConvo4(self):
        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape=self.shape, activation='relu'))
        model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(MaxPooling2D(3, 3))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def createModelConvo3(self):
        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape=self.shape, activation='relu'))
        #model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(MaxPooling2D(2, 2))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def createModelConvo2(self):
        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape=self.shape, activation='relu'))
        # model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(MaxPooling2D(4, 4))
        model.add(Flatten())
        # model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def createModelConvo1(self):
        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape=self.shape, activation='relu'))
        model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(MaxPooling2D(2, 2))
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dense(256, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def choose(self, i):
        if i == 1:
            return self.createModelConvo1()
        if i == 2:
            return self.createModelConvo2()
        if i == 3:
            return self.createModelConvo3()
        if i == 4:
            return self.createModelConvo4()
        else:
            return 0
