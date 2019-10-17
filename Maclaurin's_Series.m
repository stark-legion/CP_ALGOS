%%Calculate sum of n number of terms in Maclaurin's series and graphically show that
%%error in calculation decreases with the increasing number of terms

n=6;
a=0.1;
expval=1.0;
currentterm=1.0;
trueval=exp(0.1);

value=0;
err=0;

for i=1:n
    currentterm=currentterm*a/i;
    expval=expval+currentterm;
    error=(expval-trueval);
    disp(['Value= ',num2str(expval),'\t Error= ',num2str(abs(error))]);
end

value=[value;n];
err=[err;error];

plot(value,err,'-bo');
grid on
grid minor
xlabel('Number of terms in the series');
ylabel('Error in value');
    