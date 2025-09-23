import * as vscode from 'vscode';
import { sendCodeToServer } from './api';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('dontjustwarnme.fixCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showInformationMessage('No editor open');
            return;
        }

        const selection = editor.selection;
        const code = editor.document.getText(selection);

        if (!code.trim()) {
            vscode.window.showWarningMessage('Please select some Python code first.');
            return;
        }

        try {
            const fixed = await sendCodeToServer(code);
            editor.edit(editBuilder => {
                editBuilder.replace(selection, fixed);
            });
            vscode.window.showInformationMessage('✨ Code fixed by Don\'tJustWarnMe!');
        } catch (err: any) {
            vscode.window.showErrorMessage(`Fix failed: ${err.message}`);
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
 
