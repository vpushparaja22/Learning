function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
x1 = [1 2 1]; x2 = [0 4 -1];
results = [];
for C_test = [0.01,0.03,0.1,0.3,1,3,10,30]
    for sigma_test = [0.01,0.03,0.1,0.3,1,3,10,30]
        
        model = svmTrain(X, y, C_test, @(x1, x2) gaussianKernel(x1, x2, sigma_test));
        pred = svmPredict(model, Xval);
        error = mean(double(pred ~= yval));
        
        results = [results; C_test sigma_test error];
    end
end

fprintf('# C\tSigma\tError\n');
m = size(results, 1);
for i=1:m
    fprintf('  %f\t%f\t%f\n', results(i,1), results(i,2), results(i,3))
end

[minval, minidx] = min(results(:,3));
fprintf('Minimum values is: %f\n', minval)

C = results(minidx, 1);
sigma = results(minidx, 2);

fprintf('Minimum C is: %f\n', C)
fprintf('Minimum sigma is: %f\n', sigma)
% =========================================================================

end
