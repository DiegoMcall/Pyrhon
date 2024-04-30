/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import DTO.FuncionarioDTO;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import javax.swing.JOptionPane;

/**
 *
 * @author Aluno
 */
public class FuncionarioDAO {
    
    public void cadastrarFuncionario(FuncionarioDTO funcionariodto){
        String sql = "insert into tabela(nome, cidade) values(?,?)";
        
        Connection conn = new Conexao().conectaBD();
        
        try {
            PreparedStatement pstm = conn.prepareStatement(sql);
            pstm.setString(1, funcionariodto.getNomeFuncionario());
            pstm.setString(2, funcionariodto.getCidadeFuncionario());
            
            pstm.execute();
            pstm.close();
            
        } catch (SQLException erro) {
            
            JOptionPane.showMessageDialog(null, erro);
        }
    
    }
    
    public void excluirFuncionario(FuncionarioDTO funcionariodto){
        String dsql = "delete from tabela where nome=? and cidade=?";
        
        Connection conn = new Conexao().conectaBD();
        
        try{
            PreparedStatement pstm = conn.prepareStatement(dsql);
            pstm.setString(1, funcionariodto.getNomeFuncionario());
            pstm.setString(2, funcionariodto.getCidadeFuncionario());
            
            pstm.execute();
            pstm.close();
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, erro);
        }
    }
    
   
    
}
