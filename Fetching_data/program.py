import image_recog

test_reco = image_recog.Image_recog(
    "/Users/carlalasry/Downloads/carla1.png",
                        "/Users/carlalasry/Downloads/arthur.jpg", "/Users/carlalasry/Desktop/carla_smile.jpg", "/Users/carlalasry/Desktop/carla_not_smile.jpg")
print(test_reco.check_similarity())
#print(test_reco.similarity)
print(test_reco.check_is_smiling())
#print(test_reco.is_smiling)
