#include <iostream>
#include <vector>

using namespace std;

int calculateXOR(const vector<int>& subset) {
    int result = 0;
    for (int num : subset) {
        result ^= num;
    }
    return result;
}

void generateSubsets(const vector<int>& nums, int index, vector<int>& currentSubset, int& totalXOR) {
    if (index == nums.size()) {
        totalXOR += calculateXOR(currentSubset);
        return;
    }

    currentSubset.push_back(nums[index]);
    generateSubsets(nums, index + 1, currentSubset, totalXOR);

    currentSubset.pop_back();
    generateSubsets(nums, index + 1, currentSubset, totalXOR);
}

int subsetXORSum(const vector<int>& nums) {
    int totalXOR = 0;
    vector<int> currentSubset;
    generateSubsets(nums, 0, currentSubset, totalXOR);
    return totalXOR;
}

int main() {
    vector<int> nums = {1, 3};
    int result = subsetXORSum(nums);

    cout << "The sum of XOR totals for all subsets is: " << result << endl;

    return 0;
}