close all;
clear variables;
clc;

disp('Текст кириллицей');

data = [9 5 7 4 2 8 1 10 6 3];
n=length(data);

for scanIndex = 1:n
    minIndex = scanIndex;

    for compIndex = scanIndex+1:n
        if data(compIndex) < data(minIndex)
            minIndex = compIndex;
        end
    end
    
    if minIndex ~= scanIndex
        [data(scanIndex), data(minIndex)] = deal(data(minIndex),data(scanIndex));
        disp(data)
    end
end
