package d032;

class RDLL {
    Shape origin = null;
    int len = 0;

    private Shape setValue(int n) { // should null check
        if (n > 3 || n < 1) {
            System.out.println("error: wrong value");
            return null;
        }
        Shape temp = null;
        switch (n) {
        case 1:
            temp = new Line();
            break;
        case 2:
            temp = new Rect();
            break;
        case 3:
            temp = new Circle();
            break;
        }
        return temp;
    }

    void getValue(int index) {
        Shape temp = at(index);
        if (temp == null)
            return;
        temp.draw();
        System.out.println();
    }

    Shape at(int index) { // should null check
        if (index > len - 1 || index < -len) {
            System.out.println("error: wrong index");
            return null;
        }
        Shape temp = origin;
        if (index >= 0) {
            for (int i = 0; i < index; i++)
                temp = temp.getNext();
            return temp;
        } else {
            for (int i = 0; i < index; i++)
                temp = temp.getBefore();
            return temp;
        }
    }

    void push(int n) {
        Shape temp = setValue(n);
        if (temp == null)
            return;
        len++;
        if (origin == null) {
            origin = temp;
            origin.setBefore(temp);
            origin.setNext(temp);
        } else {
            origin.getBefore().setNext(temp);
            temp.setBefore(origin.getBefore());
            temp.setNext(origin);
            origin.setBefore(temp);
        }
    }

    void pop() {
        delete(-1);
    }

    void rotate_left() {
        origin = origin.getNext();
    }

    void rotate_left(int num) {
        for (int i = 0; i < num; i++)
            origin = origin.getNext();
    }

    void rotate_right() {
        origin = origin.getBefore();
    }

    void rotate_right(int num) {
        for (int i = 0; i < num; i++)
            origin = origin.getBefore();
    }

    void delete(int index) { // To Do
        Shape temp = at(index);
        if (temp == null)
            return;
        len--;
        if (len == 0)
            origin = null;
        else {
            temp.getBefore().setNext(temp.getNext());
            temp.getNext().setBefore(temp.getBefore());
        }
    }

    int size() {
        return len;
    }

    void show() {
        Shape b = origin;
        System.out.print("[");
        if (len == 0) {
            System.out.println("]");
        }
        for (int i = 0; i < len; i++) {
            b.draw();
            if (i != len - 1)
                System.out.print(", ");
            else
                System.out.println("]");
            b = b.getNext();
        }
    }
}