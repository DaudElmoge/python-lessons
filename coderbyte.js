/*function camelCase(str) {
  return str.replace(/\W+(.)/g, function (_, chr) {
    // The regular expression /\W+(.)/g looks for one or more non-word characters (\W+)
    // followed by any character (.), and captures that character.
    return chr.toUpperCase();
    // For each match, this function returns the captured character (chr)
    // converted to uppercase
  });
}
console.log(camelCase("Bob loves coding"));*/

function camelCase(str) {
  // First, replace spaces and capitalize the next letter after each space
  let result = str.replace(/\W+(.)/g, function (_, chr) {
    // \W+ matches one or more non-word characters (like spaces or punctuation)
    // (.) captures the next character after that
    return chr.toUpperCase(); // Capitalize the captured character
  });

  // Then, make the first letter lowercase and return the final result
  return result.charAt(0).toLowerCase() + result.slice(1);
  // charAt(0).toLowerCase() makes the first letter small
  // slice(1) keeps the rest of the string unchanged
}

// Test the function
console.log(camelCase("Bob loves coding")); // Output: "bobLovesCoding"

//string checker

function CodeLandUsernameValidator(str) {
  if (str.length < 4 || str.length > 25) {
    return "false";
  }
  if (!/^[a-zA-Z]/.test(str)) {
    return "false";
  }
  if (!/^[a-zA-Z0-9_]+$/.test(str)) {
    return "false";
  }
  if (str.endsWith("_")) {
    return "false";
  }
  return "true";
}
console.log(CodeLandUsernameValidator("Daud_Ahmed1"));
console.log(CodeLandUsernameValidator("DaudAhmed1!"));

function CodeLandUsernameValidator(str) {
  if (str.length < 4 || str.length > 25) {
    return "false";
    //if its less than 4 or more than 25 its invalid
  } else if (!/^[a-zA-Z]/.test(str)) {
    // this regular expression checks if it starts with a letter
    // If the string does NOT start with a letter, return false
    // '!' negates the result of the test

    return "false";
  } else if (!/^[a-zA-Z0-9_]+$/.test(str)) {
    //the regular expression allows only letters,numbers and underscore.
    return "false";
  } else if (str.endsWith("_")) {
    //simply checks if the string ends with an underscore
    return "false";
  } else {
    return "true";
  }
}

console.log(CodeLandUsernameValidator("Daud_Ahmed1!"));
console.log(CodeLandUsernameValidator("daudahmed"));
