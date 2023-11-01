from pdf2image import convert_from_path
import layoutparser as lp

document_pdf_path = '/Users/tylermccarthy/Desktop/Documents/MBS/Projects/KEYIS/GPU_DETECTRON/KEYIS_E3.pdf'
images = convert_from_path(document_pdf_path)

model = lp.models.Detectron2LayoutModel(
            config_path ='lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config', # In model catalog
            label_map   ={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"}, # In model`label_map`
            extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8] # Optional
        )

# Initialize an empty list to store the layouts of the documents
layouts = []

for i, image in enumerate(images):
    # Analyze layout
    layout = model.detect(image)
    layouts.append(layout)

for layout in layouts:
    print(layout)
