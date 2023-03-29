/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0]);
    const results = [];
    let lastMerged = intervals[0];
    let merged;
    for(let i = 1; i < intervals.length; i++){
        let lastMergedStart = lastMerged[0];
        let lastMergedEnd = lastMerged[1];
        let currInterval = intervals[i];
        let currIntervalStart = currInterval[0];
        let currIntervalEnd = currInterval[1];
        if(currIntervalStart <= lastMergedEnd){
            
            if(currIntervalEnd < lastMergedEnd){
                merged = lastMerged;
            }else{
                merged = [lastMergedStart, currIntervalEnd];
            }
            lastMerged = merged;
            
        }else{
            
            results.push(lastMerged);
            lastMerged = currInterval;
            
        }
    }
    
    results.push(lastMerged);
    
    return results;
};