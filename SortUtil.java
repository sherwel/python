package itfriday.crazyz;

public class SortUtil {
	//���롣ע�⣺��Ԫ�غ��ƣ����滻Ԫ�أ�ע���滻Ԫ�ص�ԭʼֵ��
	public static int[] insert(int[] array){
		for(int i=1;i<array.length;i++){
		   int j = i-1;
		   int temp = array[i];
		   //Ԫ�غ���
	       for(;j>=0;j--){
	    	   if( array[i]<array[j]){
	    		   array[j+1] = array[j];
	    	   }else{
	    		   break;
	    	   }
	       }
	       //�滻����
	       array[j+1] = temp;
		}
		return array;
	}
	
	//��ѡ��
	public static int[] simpleChoice(int[] array){
		for(int i=0;i<array.length;i++){
			for(int j=i;j<array.length;j++){
				if(array[i]>array[j]){
					array[i] = array[i]^array[j];
					array[j] = array[i]^array[j];
					array[i] = array[i]^array[j];
				}
			}
		}
		return array;
	}
	public static String[] simpleChoice(String[] array){
		for(int i=0;i<array.length;i++){
			for(int j=i;j<array.length;j++){
				if(array[i].compareTo(array[j])>0){
					String temp = array[i];
					array[i] = array[j];
					array[j] = temp;
				}
			}
		}
		return array;
	}
	
	
	//ð��
	public static int[] bubble(int[] array){
		for(int i=0;i<array.length-1;i++){
			for(int j=0;j<array.length-1;j++){
				if(array[j]>array[j+1]){
					array[j] = array[j]^array[j+1];
					array[j+1] = array[j]^array[j+1];
					array[j] = array[j]^array[j+1];
				}
			}
		}
		return array;
	}
	public static String[] bubble(String[] array){
		for(int i=0;i<array.length-1;i++){
			for(int j=0;j<array.length-1;j++){
				if(array[j].compareTo(array[j+1])>0){
					String temp = array[i];
					array[i] = array[i]+1;
					array[i+1] = temp;
				}
			}
		}
		return array;
	}
	
	public static void main(String[] args) {
		int[] array = {1,3,2,4};
		array = insert(array);
		for(int i:array){
			System.out.println(i);
		}
	}
}
