from skyWriting import skyWrite
# from autoCorrect import autoCorrect
# from textGetter import detect_text
from main_detect import infer_by_web

def main():
    print("executing the values inside main")
    skyWrite()
    print("here")
    text="/home/local/ZOHOCORP/divya-pt5022/divya-files/text-writing-detection-air-dl/Text-writing/output/temp.png"
    print(text)
    option="bestPath"
    result = predict_image(text, option)
    # text = autoCorrect(text)
    print(result)
    return result 

def predict_image(path, type):
    print(path)
    result = infer_by_web(path, type)
    print("inside write file", result)
    return result


if(__name__=="__main__"):
    main()