function f = predictor_fitness(coeffs)
  global training;
  f = 0;
  for r = 1:size(training,1) 
	 prediction = dot(coeffs,training(r,1:4)) ./ sum(coeffs);
         f = f + (training(r,5) - prediction) .^ 2;
  end; 
  f = f ./ size(training,1);
