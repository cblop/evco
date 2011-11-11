function prediction = mypredictor(recent)

        coeffs = [1 3 5 7];
	prediction = dot(coeffs,recent) ./ sum(coeffs)
        % note: the MATLAB function dot performs the scalar product, i.e. matrices
        % are multiplied element-wise and the results summed together

	% replace this with a function of your choice
        % note: recent(4) is the most recent data point
	
