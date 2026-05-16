/*const story = document.querySelector('.story');

const setText = document.querySelector('#set-text');
setText.addEventListener('click', () => {
    story.textContent = 'It was a dark night and stormy night';
})

const clearText = document.querySelector('#clear-text');
clearText.addEventListener('click', () => {
    story.textContent = '';
})*/

const parent = document.querySelector('.parent');

const addChild = document.querySelector('#add-child');
addChild.addEventListener('click', () => {
    // Only add a child if we don't already have one, in addition to the text node "parent"
    if (parent.childNodes.length > 1) {
        return;
    }
    const child = document.createElement("div");
    child.classList.add("child");
    child.textContent = "child";
    parent.appendChild(child);
})

const removeChild = document.querySelector('#remove-child');
removeChild.addEventListener('click', () => {
    const child = document.querySelector('.child');
    parent.removeChild(child);
})

function stopEvent(event) {
    const c2 = document.getElementById("c2");
    c2.textContent = "Hello World!";

    event.stopPropagation();
    console.log("event propagation halted.");
}

const elem = document.getElementById("tbl1");
elem.addEventListener("click", stopEvent);

document.getElementById("t-dad").addEventListener("click", () => {
    console.log("t-dad clicked");
});
