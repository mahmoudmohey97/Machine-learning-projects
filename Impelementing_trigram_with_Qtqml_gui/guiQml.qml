import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 1.4

Window{
    visible: true
    width: 800
    height: 500

    Image{
        source: "f.jpg"
        anchors.fill: parent
    }

    TextInput {
        id: textInput
        x: 473
        y: 217
        width: 233
        height: 54
        text: "write here"
        Keys.onReleased: {
            qml.getSearchSentence(textInput.text.toString())
            //textInput.text = (textInput.text + " ").toString()
            var result = qml.getResults()
            result = result.split(" ")
            if(result.length > 1){
                var i = 0
                var hold = ""
                for(i = 0; i < result.length - 1 ; i++){
                    hold += (textInput.text + " " +result[i] + '\n').toString()
                }
                element.text = hold
            }
            else
                element.text = ""
        }

        font.pixelSize: 12
    }

    TextArea {
        id: element
        x: 32
        y: 315
        width: 433
        height: 147
          }

    Text {
        id: element1
        x: 296
        y: 36
        width: 156
        height: 44
        color: "#b70000"
        text: qsTr("MAH engine")
        font.bold: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 16
    }
}


