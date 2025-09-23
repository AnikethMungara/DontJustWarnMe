"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.sendCodeToServer = void 0;
const node_fetch_1 = __importDefault(require("node-fetch"));
async function sendCodeToServer(code) {
    const response = await (0, node_fetch_1.default)('http://localhost:5000/fix_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
    });
    if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
    }
    const data = (await response.json());
    return data.fixed_code;
}
exports.sendCodeToServer = sendCodeToServer;
