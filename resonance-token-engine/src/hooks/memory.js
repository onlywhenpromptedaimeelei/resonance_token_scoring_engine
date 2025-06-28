export function retrieveMemory(key) {
return localStorage.getItem(key);
}
export function storeMemory(key, value) {
localStorage.setItem(key, value);
}
