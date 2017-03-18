class Category:
	def __init__(self, categoryYaml, weighting, pixelMap) #category weighting must be passed in by chart, not set in stone
		self.categoryYaml      = categoryYaml
		self.name              = categoryYaml['category']
		self.weighting         = weighting
		self.pixelMap          = pixelMap
		self.elements          = self.__getElements() #hash of tuples -- each key corresponds to the 'You' and 'Them' versions of an element
		self.elementWeightings = self.__getElementWeightings()
		
	#TODO: pretty ugly
	def __getElements(): #Yaml format is different for each element type
		elements = {}
	
		checkboxSetsYaml = categoryYaml['checkboxSets']
		for checkboxSetYaml in checkboxSetsYaml
			elements[checkboxSetYaml['name']] = CheckboxSet.getYouAndThemElementsFromYaml(checkboxSetYaml)
		
		pictographicCheckboxSetsYaml = categoryYaml['pictographicCheckboxSets']
		for pictographicCheckboxSetYaml in pictographicCheckboxSetsYaml
			elements[pictographicCheckboxSetYaml['name']] = PictographicCheckboxSet.getYouAndThemElementsFromYaml(pictographicCheckboxSetYaml)
		
		numericalRangeBars = categoryYaml['numericalRangeBars']
		for numericalRangeBarYaml in numericalRangeBarsYaml
			elements[numericalRangeBarYaml['name']] = NumericalRangeBar.getYouAndThemElementsFromYaml(numericalRangeBarYaml)
		
		fuzzyRangeBars = categoryYaml['fuzzyRangeBars']
		for fuzzyRangeBarYaml in fuzzyRangeBarsYaml
			elements[fuzzyRangeBarYaml['name']] = FuzzyRangeBar.getYouAndThemElementsFromYaml(fuzzyRangeBarYaml)
		
		twoDFuzzyRangeBars = categoryYaml['twoDFuzzyRangeBars']
		for twoDFuzzyRangeBarYaml in twoDFuzzyRangeBarsYaml
			elements[twoDFuzzyRangeBarYaml['name']] = TwoDFuzzyRangeBar.getYouAndThemElementsFromYaml(twoDFuzzyRangeBarYaml)
	
	def __getElementWeightings():
		for elementTypeYaml in categoryYaml
			for elementYaml in elementTypeYaml
				elementRelativeWeightings[elementYaml['name']] = elementYaml['weighting']
				
		return Chart.weightingsFromRelativeWeightings(elementRelativeWeightings)
		
	def scoreCategory(theirCategory):
		totalCategoryScore = 0.0
		for elementName,elementPair in self.elements
			totalCategoryScore += elementPair[0].scoreElement(elementPair[1]) #'You' scores 'Them'
			totalCategoryScore *= self.weighting
			
		return totalCategoryScore