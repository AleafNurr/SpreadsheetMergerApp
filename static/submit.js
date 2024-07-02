let dropZone1 = document.getElementById("drop-zone-1");
let dropZone2 = document.getElementById("drop-zone-2");

let fileInput1 = document.getElementById("file-input-1");
let fileInput2 = document.getElementById("file-input-2");

let uploadForm = document.getElementById("uploadForm");

dropZone1.addEventListener("click", function () {
    fileInput1.click();
});

dropZone2.addEventListener("click", function () {
    fileInput2.click();
});

fileInput1.addEventListener("change", function () {
    if (fileInput1.files.length > 0){
        console.log("change");
        // uploadForm.submit();
    }
});

fileInput2.addEventListener("change", function () {
    if (fileInput2.files.length > 0){
        console.log("change");
        // uploadForm.submit();
    }
});

dropZone1.addEventListener("dragover", function (e) {
    e.preventDefault();
    this.classList.add("dragover");
});

dropZone2.addEventListener("dragover", function (e) {
    e.preventDefault();
    this.classList.add("dragover");
});

dropZone1.addEventListener("dragleave", function (e) {
    e.preventDefault();
    this.classList.add("dragleave");
});

dropZone2.addEventListener("dragleave", function (e) {
    this.classList.add("dragleave");
});

dropZone1.addEventListener("drop", function (e) {
    e.preventDefault();
    e.stopPropagation();
    console.log("drop leave")
    this.classList.remove("dragover");

    let file = e.dataTransfer.files[0];
    fileInput1.files = e.dataTransfer.files;
    console.log(file);
    // uploadForm.submit();
});

dropZone2.addEventListener("drop", function (e) {
    e.preventDefault();
    e.stopPropagation();
    this.classList.remove("dragover");

    let file = e.dataTransfer.files[0];
    fileInput2.files = e.dataTransfer.files;
    // uploadForm.submit();
});