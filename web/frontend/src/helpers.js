export function joinArraysWithoutDuplicates(array1, array2) {
    const combinedArray = array1.concat(array2);
    const uniqueArray = combinedArray.filter((item, index) => combinedArray.indexOf(item) === index);

    return uniqueArray;
}

export function formatString(inputWord) {
    const parts = inputWord.split('_');

    const convertedParts = parts.map(part => {
        return part.charAt(0).toUpperCase() + part.slice(1).toLowerCase();
    });

    const convertedWord = convertedParts.join(' ');

    return convertedWord;
}