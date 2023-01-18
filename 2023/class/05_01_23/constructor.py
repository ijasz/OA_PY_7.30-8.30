class Mobile:
    def __init__(self, brandName, storage):
        self.brandName = brandName
        self.storage = storage

    def mobileDetails(self):
        print(f"Brandname - {self.brandName}")
        print(f"storage - {self.storage}")


obj1 = Mobile("oneplus", "1TB")
obj2 = Mobile("oneplus", "500GB")

obj1.mobileDetails()
obj2.mobileDetails()
print(obj1)
      ``
