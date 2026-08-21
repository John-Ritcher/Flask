/*const story = document.querySelector('.story');

const setText = document.querySelector('#set-text');
setText.addEventListener('click', () => {
    story.textContent = 'It was a dark night and stormy night';
})

const clearText = document.querySelector('#clear-text');
clearText.addEventListener('click', () => {
    story.textContent = '';
})*/

/*const parent = document.querySelector('.parent');

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
});*/


const button = document.querySelector(".showHide");
const contents = document.querySelector(".cont_m");

const backup = contents.innerHTML;

if (button)
{
    button.addEventListener("click", () => {
    if (button.textContent === "Show") {
        button.textContent = "Hide";
  //      contents.textContent = ""; Ruim comparado com style.display = "none"
         contents.style.display = "none";
    }
    else if (button.textContent === "Hide") {
        button.textContent = "Show";
 //       contents.innerHTML = backup;  Solução que eu pensei mas que não consegui chegar, tiveram que me mostrar
        contents.style.display = "table"; //esse é superior, não precisa remover o texto
    }
})
}

const tabs = document.querySelectorAll(".changeImg li");
const tabs2 = document.querySelectorAll(".changeImg2 li");

tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        const gallery = tab.closest(".gallery");
        const galleryTabs = gallery.querySelectorAll(".changeImg li")
        const myImage = gallery.querySelector(".character-image");
        const mySrc = myImage.getAttribute("src");
        const newSrc = tab.dataset.src;
        galleryTabs.forEach(t => t.classList.remove("active"))
        if (mySrc !== newSrc)
        {
            myImage.setAttribute("src", newSrc);
            tab.classList.add("active");
        }
    })
})

const tables = document.getElementsByTagName("ul");
const firstTable = tables.item(1); // or tables[1] - returns the second table in the DOM
console.log(firstTable);