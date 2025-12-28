const BACKGROUND = "#101010"
const FOREGROUND = "#50FF50"
// const gameFixedSize = 800
// game.width = gameFixedSize;
// game.height = gameFixedSize;

game.width = window.innerWidth;
game.height = window.innerHeight;
const ctx = game.getContext("2d") // 2D API for js canvas, 3D is WebGLs
console.log(game)
console.log(ctx)

function clear() {
    ctx.fillStyle = BACKGROUND
    ctx.fillRect(0, 0, game.width, game.height)
}

function printRectangle({ x, y, w = 20, h = 20 }) {
    ctx.fillStyle = FOREGROUND
    // the minus size/2 its to avoid the point disappearing over the screen limits
    ctx.fillRect(x - w / 2, y - h / 2, w, h)
}

// points location on the screen varies from -1 to 1 in a cartesian plane
// so: all to the left its the point x: -1, y: any, and all up its x: any, t: 1
function screen(point) {
    return {
        x: ((point.x + 1) / 2) * game.width,
        y: (1 - (point.y + 1) / 2) * game.height,
    }
}

// p1 (small triangle) follows the proportion between similar triangle
// since it has the same angles as p2 (big triangle), so we can derive the equation:
// x´ = x/z and y´=y/z since X/x = Y/y = Z/z with z = 1
//
//(x,y)|    |(screen)--->
//     |    |/ | <-- projection in p1 of the point in z to p2
//     |  / |  |
// eye o/_p1|p2|_ _ _ _ _ ---> (z projection inside the screen...)
//    z| z=1|
//
// z can´t be zero since it will not project anything since it's at the same
// level as the "eye". z = 1 its at the screen leven
//
//
// i.e, this two points give the same projection since they are straight from the eye
// printRectangle(screen(project({ x: 0, y: 0, z: 1 })))
// printRectangle(screen(project({ x: 0, y: 0, z: 2 })))
function project({ x, y, z }) {
    return {
        x: x / z,
        y: y / z,
    }
}

function drawLine(p1, p2) {
    ctx.lineWidth = 3
    ctx.strokeStyle = FOREGROUND
    ctx.beginPath()
    ctx.moveTo(p1.x, p1.y)
    ctx.lineTo(p2.x, p2.y)
    ctx.stroke()
}

function translate_z({ x, y, z }, dz, direction = 1) {
    return { x, y, z: z + (dz * direction) }
}

// to rotate in one axis, use the other ones
// rotate in x
function rotate_yz({ x, y, z }, angle) {
    const c = Math.cos(angle)
    const s = Math.sin(angle)
    return {
        x: x,
        y: y * c - z * s,
        z: x * s + z * c,
    }
}

// rotate in y
function rotate_xz({ x, y, z }, angle) {
    const c = Math.cos(angle)
    const s = Math.sin(angle)
    return {
        x: x * c - z * s,
        y,
        z: x * s + z * c,
    }
}

function transformPoints(point, angle, dz) {
    // first apply any rotation
    // then translate z from p2 to p1 (inside the screen to the exact screen point z = 1)
    // then transform the x and y to the z plane
    // then normalize the point in the screen canvas dimensions
    return screen(project((translate_z(rotate_xz(point, angle), dz))))
}

function printVertices(vertices, angle, dz) {
    for (const v of vertices) {
        printRectangle(transformPoints(v, angle, dz))
    }
}

function printLines(vertices, faces, angle, dz) {
    for (const f of faces) {
        for (let i = 0; i < f.length; ++i) {
            const a = vertices[f[i]]
            const b = vertices[f[(i + 1) % f.length]]
            drawLine(
                transformPoints(a, angle, dz),
                transformPoints(b, angle, dz),
            )
        }
    }
}

const vertices = [
    { x: 0.5, y: 0.5, z: 0.5 },
    { x: -0.5, y: 0.5, z: 0.5 },
    { x: -0.5, y: -0.5, z: 0.5 },
    { x: 0.5, y: -0.5, z: 0.5 },

    { x: 0.5, y: 0.5, z: -0.5 },
    { x: -0.5, y: 0.5, z: -0.5 },
    { x: -0.5, y: -0.5, z: -0.5 },
    { x: 0.5, y: -0.5, z: -0.5 },
]

const faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],

    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]
const FPS = 60
const dt = 1 / FPS // delta time between two frames

// dz or z offset:
//  positive dz means its getting farther away
//  negative dz means its getting closer
let dz = 1
let angle = 0
function frame() {
    dz += 1 * dt // comment if you don't want any projection
    angle += 2 * Math.PI * dt

    // reset screen
    clear()

    // print stuff
    printVertices(vertices, angle, dz)
    printLines(vertices, faces, angle, dz)

    // callback to next frame
    setTimeout(frame, 1000 / FPS)
}

setTimeout(frame, 1000 / FPS)
