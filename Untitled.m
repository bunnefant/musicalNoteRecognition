% Inputs: a side (A) and a hypotenuse (C)
% Outputs: the other side (B) rounded to 2 decimals;

function B = Untitled(A, C)
    %B_squared = C^2-A^2;
    B = sqrt(C^2-A^2);
    B = round(B, 2);
end