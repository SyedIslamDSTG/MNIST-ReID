# MNIST-ReID
MNIST-ReID is constructed based on the existing MNIST [1] digit dataset to assess whether a gallery-set based ReID method actually combines the information from multiple observations. The main challenge is that individual observations lack sufficient information for identification, while the full gallery-set provides it. Any successful method must be able to integrate information across multiple observations.

We consider images containing two handwritten digits, one red and one green, defining 100 identities (00-99). The red digit represents the first digit of the identity, while the green digit represents the second. An observation can appear in one of three modalities: red, which reveals only the first digit; green, which reveals only the second digit; and RG, which reveals both digits and therefore fully specifies the identity. We have two versions of this dataset:
1. mnist_reid.pkz: As described above.
2. mnist_reid_C.pkz: A corrupted and more difficult version of the above dataset. This overlaps the expected digits for the 'red' and 'green' observations with an additional random digit. For any two 'red' observations for a given ID, the added digit will most likely be different, so the correct digit may be inferred. This means that it would be necessary for a gallery-set based ReID method to combine information from at least four different observations (two red, and two green) to perfectly identify the object.
   
By desgin, this dataset has 100 IDs, 15 of which are specific to the test set and are used for queries. The training data has 45,441 observations split between "rg", "red" and "green" types. The test data has 3,431 query images of type "rg" corresponding to 15 IDs and a further 3,000 images (a gallery-set of size 30 per ID) of all 100 IDs for just “red” and “green” types. 

References
[1] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-Based Learning Applied to Document Recognition,” Expert Systems With Applications, November, 1998.

Cite this dataset as
@INPROCEEDINGS{GalSetReID,
  author={Islam, Syed Imranul and Cooke, Tristrom and  and Islam, Kazi Yasin and Asikuzzaman, Md and Williams, Jerome and Yip, Ben and Cao, Tri-Tan and Wong, Sebastien},
  booktitle={DICTA 2026}, 
  title={{Gallery-Set Based Re-Identification}}, 
  year={2026},
  volume={},
  number={},
  pages={},
}

