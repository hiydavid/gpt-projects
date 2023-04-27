//
//  chatapp.swift
//

import SwiftUI

struct ContentView: View {
    @State var chatMessages: [ChatMessage] = ChatMessage.sampleMessages
    @State var messageText: String = ""
    
    var body: some View {
        VStack{
            ScrollView{
                LazyVStack {
                    ForEach(chatMessages, id: \.id) {
                        message in messageView(message: message)
                    }
                }
            }
            HStack {
                TextField("Enter a message", text: $messageText) {
                    
                }
                    .padding()
                    .background(.gray.opacity(0.1))
                    .cornerRadius(12)
                Button {
                    sendMessage()
                } label: {
                    Text("Send")
                        .foregroundColor(.white)
                        .padding()
                        .background(.black)
                        .cornerRadius(12)
                }
            }
        }
        .padding()
    }
    
    func messageView(message: ChatMessage) -> some View {
        HStack{
            if message.sender == .me { Spacer() }
            Text(message.content)
                .foregroundColor(message.sender == .me ? .white : .black)
                .padding()
                .background(message.sender == .me ? .blue : .gray.opacity(0.1))
                .cornerRadius(16)
            if message.sender == .gpt { Spacer() }
        }
    }
    
    func sendMessage() {
        messageText = ""
        print(messageText)
    }
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

struct ChatMessage {
    let id: String
    let content: String
    let dateCreated: Date
    let sender: MessageSender
}

enum MessageSender {
    case me
    case gpt
}

extension ChatMessage {
    static let sampleMessages = [
        ChatMessage(
            id: UUID().uuidString,
            content: "Hello, sir! What's up?",
            dateCreated: Date(),
            sender: .gpt),
        ChatMessage(
            id: UUID().uuidString,
            content: "My kid is screaming and doesn't want to eat dinner. What should I do?",
            dateCreated: Date(),
            sender: .me),
        ChatMessage(
            id: UUID().uuidString,
            content: "...",
            dateCreated: Date(),
            sender: .gpt),
    ]
}
