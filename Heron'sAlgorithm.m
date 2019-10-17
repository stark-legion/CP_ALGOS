%%Calculate sqrt(2) using Heron's Algorithm 


x=0.5;
etoll=1.0e-5;
err=1;


while (err>etoll)
    xnew=1/2*(x+2/x);
    err=abs(x-xnew;)
    x=xnew;
end

