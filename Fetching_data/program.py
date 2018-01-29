from image_recognition import image_recog

test_reco = image_recog.Image_recog("data/half_closed.jpg",
                                    "data/arthur.jpg",
                                    "data/arthur.jpg")
print(test_reco.is_similar())
#print(test_reco.similarity)
print(test_reco.is_smiling_ratio())
#print(test_reco.is_smiling)
